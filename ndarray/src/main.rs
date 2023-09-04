use polars::prelude::*;

fn main() -> Result<()> {
    let file_path = "path/to/your/csvfile.csv";
    let df = CsvReader::from_path(file_path)?
        .infer_schema(Some(16))
        .finish()?;
    
    println!("{:?}", df);
    Ok(())
}
