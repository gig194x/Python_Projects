def test_input_validation():
    print("=== Running Input Validation Tests ===")
    
    system = GradeSystem()
    
    #Student ID  
    try:
        system.add_student("abc", "Ali")  
        print("Failed: Non-numeric Student ID accepted")
    except:
        print("Passed: Non-numeric Student ID rejected")
    
    #Student Name 
    try:
        system.add_student(1, 12345) 
        print("Failed: Numeric name accepted")
    except:
        print("Passed: Numeric name rejected")
    
    #Grade btw 0,100
    system.add_student(2, "Sara")  
    try:
        system.add_grade(2, "Math", "A+")  
        print("Failed: Non-numeric grade accepted")
    except:
        print("Passed: Non-numeric grade rejected")
    
    try:
        system.add_grade(2, "Math", 150)  
        print("Failed: Grade >100 accepted")
    except:
        print("Passed: Grade >100 rejected")
    
    try:
        system.add_grade(2, "Math", -10)  
        print("Failed: Grade <0 accepted")
    except:
        print("Passed: Grade <0 rejected")
    
    print("Input Validation Tests Completed")


if __name__ == "__main__":
    test_input_validation()
