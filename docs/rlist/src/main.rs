// @filename    :  main.rs
// @author      :  Copyright (C) Church.ZHONG
// @date        :  2024-04-16
// @required    :  rustc 1.77.2
// @function    :  as same as `ls -t | grep mime`

use clap::Parser;
use std::fs;
use std::path::Path;

/// <https://man7.org/linux/man-pages/man1/ls.1.html>
///
/// --time=WORD
///       select which timestamp used to display or sort; access
///       time (-u): atime, access, use; metadata change time (-c):
///       ctime, status; modified time (default): mtime,
///       modification; birth time: birth, creation;
///
///       with -l, WORD determines which time to show; with
///       --sort=time, sort by WORD (newest first)

#[allow(clippy::collapsible_else_if)]
#[allow(clippy::manual_flatten)]
fn list_files(path: &Path, all: &bool, prefix: &String, suffix: &String) -> Vec<String> {
    let mut files = Vec::new();

    if let Ok(entries) = fs::read_dir(path) {
        for entry in entries {
            if let Ok(entry) = entry {
                let file_path = entry.path();
                let file_name = file_path.file_name().unwrap().to_string_lossy().to_string();

                if file_path.is_dir() {
                    files.extend(list_files(&file_path, all, prefix, suffix));
                } else {
                    if !ignore(&file_name, all, prefix, suffix) {
                        files.push(file_path.to_string_lossy().into_owned());
                    }
                }
            }
        }
    }

    files
}

#[allow(clippy::if_same_then_else)]
fn ignore(filename: &str, all: &bool, str_prefix: &String, str_suffix: &String) -> bool {
    // sanity check
    if !all && filename.starts_with('.') {
        return true;
    }

    // println!("# filename = {}", filename);
    // println!("# prefix   = {}", str_prefix);
    // println!("# suffix   = {}", str_suffix);

    if !str_prefix.is_empty() && !filename.starts_with(str_prefix) && str_suffix.is_empty() {
        return true;
    } else if str_prefix.is_empty() && !str_suffix.is_empty() && !filename.ends_with(str_suffix) {
        return true;
    } else if !str_prefix.is_empty()
        && !filename.starts_with(str_prefix)
        && !str_suffix.is_empty()
        && !filename.starts_with(str_prefix)
    {
        return true;
    }

    false
}

/// Simple program to list all files.
#[derive(Parser)]
#[command(author = "Church", version = "0.0.1", about, long_about = None)]
struct Args {
    /// input directory
    #[arg(short, long)]
    input: String,
    /// list all files(includes hidden)
    #[arg(short, long, default_value_t = false, help = "list all files(includes hidden)")]
    all: bool,
    /// filter by prefix (any string)
    #[arg(short, long, help = "filter by prefix (any string)")]
    prefix: Option<String>,
    /// filter by suffix (any string)
    #[arg(short, long, help = "filter by suffix (any string)")]
    suffix: Option<String>,
}

fn main() {
    // sanity check
    // /usr/include/asm-generic/errno.h
    // #define	ENOENT		 2	/* No such file or directory */
    let args = Args::parse();
    let path = Path::new(&args.input);
    if !path.exists() || !path.is_dir() {
        std::process::exit(2);
    }

    let mut prefix = String::from("");
    if let Some(take_prefix) = args.prefix {
        // println!("# prefix   = {}", take_prefix);
        prefix = take_prefix;
    }

    let mut suffix = String::from("");
    if let Some(take_suffix) = args.suffix {
        // println!("# suffix   = {}", take_suffix);
        suffix = take_suffix;
    }
    let entries = list_files(path, &args.all, &prefix, &suffix);

    /*
        for file in entries {
            println!("{}", file);
        }
    */
    let mut files: Vec<_> = entries
        .iter()
        .filter_map(|file| {
            // println!("file = {}", file);
            if let Ok(metadata) = fs::metadata(file) {
                if metadata.is_file() {
                    return Some((file, metadata));
                }
            }
            None
        })
        .collect();

    // sort by mtime
    files.sort_by(|a, b| {
        let mtime_a = a.1.modified().unwrap();
        let mtime_b = b.1.modified().unwrap();
        mtime_b.cmp(&mtime_a)
    });

    // print sorted files
    for (file, _) in files {
        let path = Path::new(file);
        let left = path.strip_prefix(&args.input).unwrap();
        println!("{}", left.display());
        //println!("{}", path.file_name().unwrap().to_string_lossy());
    }
    std::process::exit(0);
}
