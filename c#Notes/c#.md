# Variables and Data Types in C#

## C# is statically typed

```csharp
int x = 10; // Integer  
String y = "Name"; // String  
double z = 3.14; // Float  
```

In C#, it automatically converts from non-string to string if you are using `+` operators.  
If you are using `(x + y)` it cannot be overloaded because in C# it is called overloaded.

## Params
Params allow passing zero or more arguments to a method without explicitly wrapping.

## Data Type Conversion
Passing refers to converting one data type to another.

### Different Conversion Types
- String to int, float, etc.

### Common Examples

#### Explicit Parsing
Using methods like `int.Parse()`, `float.Parse()` in C#.

#### Try Parsing
Using methods like `int.TryParse()` for safe parsing and better error handling.

Example:
```csharp
String num = "123";  
if (int.TryParse(num, out int Result)) {  
    Console.WriteLine(Result);  
}
```
## Variable Declaration and Input/Output in C#

### Declaring Variables
We can declare the variable first and use it later:
```csharp
int Number;  
if (int.TryParse(Num, out Number)) {  
    Console.WriteLine(Number);  
}  
```
`out` is the parameter that allows you to return additional values in a result via a reference variable.

### Input/Output Acceptance by C#

### Examples:
```csharp
Console.WriteLine("Enter the Gildage:");  
String Gildage = Console.ReadLine();  
Console.WriteLine("Enter the bayage:");  
String bayage = Console.ReadLine();  
Console.WriteLine(Gildage + bayage);  
```

### Note:
We cannot directly pass the argument message in the `Console.ReadLine()`.
Example:
```csharp
String Gildage = Console.ReadLine("Enter the age");
```

### Options to Convert
There are several options to handle conversion:
- From data type  
- Using `Convert` class  
- `Parse`  
- Using **string interpolation**


## C# String and Data Type Manipulation

### Concatenation of Strings and Integers
You can concatenate integers and strings using the `+` operator. For example:

```csharp
int Time = 20;
String Name = "20";
System.Console.WriteLine(Time + Name);
```
In this case, the `+` operator treats the integer `Time` as a string and concatenates it with `Name`.

### String Interpolation
You can also use string interpolation for better readability:

```csharp
Console.WriteLine($"Time: {Time}, Name: {Name}");
```
This will print both the `Time` and `Name` values.

---

### String Data Type: Access and Manipulation

### Concatenation Example
```csharp
String a = "123";
String b = "456";
System.Console.WriteLine(a + b);
```
This will work, and the output will be `123456`. However, concatenating a string with an integer directly might cause an error.

---

### Changing Case: Upper and Lower Case
You can manipulate the case of a string using `ToUpper()` and `ToLower()` methods:

```csharp
String Message = "Manoj";
Message = Message.ToUpper(); // Converts to "MANOJ"
Message = Message.ToLower(); // Converts to "manoj"
```

### Important Note:
If you try to print two manipulated versions of the string like this:

```csharp
Console.WriteLine(Message1); // Message1: Uppercase
Console.WriteLine(Message2); // Message2: Lowercase
```

It **will not work** because the variables `Message1` and `Message2` are not explicitly defined. To fix this, assign each transformation to a separate variable:

```csharp
String Message = "Manoj";
String UpperMessage = Message.ToUpper();
String LowerMessage = Message.ToLower();
Console.WriteLine(UpperMessage); // Output: "MANOJ"
Console.WriteLine(LowerMessage); // Output: "manoj"
```

### Boolean

```csharp
bool isAdmin = true;
bool isAdmin = false;
```

### Example

```csharp
int age = 18;
bool isAdult = false;
if(age=>19){
    isAdult=true;
}else{
    isAdult = false;
}
```



