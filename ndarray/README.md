## 1. Importing library 

**rust**
```
use polars::prelude::*;
```
<p>
This line imports all the items from  '**prelude**' module in the "**polars**" library. "**polars**" is data processing library
frequently used for data analysis in Rust. The "prelude" module contains a collection of the most commonly used types and functions within in this library.
</p>

## 2. Main Function
**rust**
```
fn main() -> Result<()> {
```
<p>
This defines the "**main**" function, which is entry point of a Rust program. This function returns a "**Result<(), ()>**" ,which means it can return either "**Ok(())**". This is used to handle any erros that might occur during the excecution of the program.
</p>

## 3. Defining The Path to file
**rust**
```
let file_path = "path/to/your/csvfile.csv";
```
<p>
This line defines a variable "**file_path**" which contains the path to the CSV file that you want to read
</p>

## 4. Reading The CSV File
**rust**
```
let df = CsvReader::from_path(file_path)>
      .infer_schema(Some(16))
      .finish()?;
```
<p>
Here, you use the "**from_path**" method of the "**CsvReader**" class to read the CSV File from given path. The "**infer_schema**" method is used to analyze the first few rows (in this case, 15) to dermine the schema (data tpes for each column) of the data. Afterwards, the "**finish**" method is called to complete the file reading process and return a dataframe. The question mark ("**?**") after these  methods is used to propagate any errors that might occur during these calls, which would halt the execution of the program.
</p>

## 5. Displaying the Dataframe
**rust**
```
println!("{:?}",df);
```
<p>
This print the "**Debug**" representation of the dataframe to the console
</p>

## Returning Ok
**rust**
```
Ok(())
}
```
<p>
This final line returns "**Ok(())**", including that the program has succesfully run.
</p>

## How to Run
1. Ensure you have rust and Cargo (the Rust package manager) installed. You can dowlaod them from the **[Rust Website](https://www.rust-lang.org/tools/install)**
2. Create a new project with the command 'cargo new my_project'.
3. Open the 'Cargo.toml' file and add 'polars' as a dependency;
   **toml**
   ```
   [dependencies]
   polars = "0.14.0"
   ```
4. Copy your code into the 'src/main.rs' file
5. Run the program with the command 'cargo_run' ini the project directory

<p>
Now you should be able to succesfully run your program. Remember to replace "path/to/your/csvfile.csv" with  the actual path to your CSV file.
</p>
