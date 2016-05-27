# Plugins

## BlockJump
* `CTRL` + `[` :  jump up
* `CTRL` + `]` :  jump down

## KZLinkedConsole
```swift
#if DEBUG
func print(message: String, filename: String = #file, line: Int = #line, function: String = #function) {
    Swift.print("\((filename as NSString).lastPathComponent):\(line) \(function):\r\(message)")
}
#endif```

## XToDo
`//TODO:` and `//FIXME:`
Check all by `^T`
