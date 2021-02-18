from Teacher import Teacher 

def main():

    andres = Teacher("Andriy Andres", 55, "male", 25, "San-Andres", "PE")
    kuba = Teacher("Nataliya Kuba", 30, "female", 8, "sonechko", "presentation")
    nytrebych = Teacher("Zinoviy Nytrebych", 60, "male", 30, "Ninadych", "High meth") 
    veres = Teacher("Zenoviy Veres", 42, "male", 85, "Oh Great Veres", "everything")
    
    a = Teacher.display_output_of_greeting()
    print(veres.__str__(), "\n", andres.__str__(), "\n", nytrebych.__str__(), "\n", kuba.__str__())
    print(a)

if __name__ == "__main__":
    main()