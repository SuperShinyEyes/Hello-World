import UIKit

public enum ValidationResult
{
    case Valid
    case Invalid(errorMessage:String)
}

public func ==(lhs: ValidationResult, rhs: ValidationResult) -> Bool {
    switch (lhs, rhs) {
    case (.Valid, .Valid): return true
    default: return false
    }
}

protocol FormFieldType
{
    associatedtype Type
    
    var value: Type? { get set }
    
    func validate() -> ValidationResult
}

class TextField: UIView, FormFieldType {
    typealias Type = String
    
    var value: String?
    
    func validate() -> ValidationResult {
        return .Valid
    }
}

class DatePicker: UIControl, FormFieldType {
    typealias Type = NSDate
    
    var value: NSDate?
    
    func validate() -> ValidationResult {
        return .Valid
    }
}

let firstName = TextField()
let lastName = TextField()
let date = DatePicker()

//let fields: [FormFieldType] = [firstName, lastName, date]

struct AnyField {
    private let _validate: () -> ValidationResult
    
    init<Field: FormFieldType>(_ field: Field) {
        self._validate = field.validate
    }
    
    func validate() -> ValidationResult {
        return _validate()
    }
}

let fields = [AnyField(firstName), AnyField(lastName), AnyField(date)]
if fields.reduce(true, combine: { ($1.validate() == .Valid) && $0 }) {
    print("Form is valid 🎉")
}

