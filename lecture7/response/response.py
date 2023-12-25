import validators

def main():
    print(validemail(input("What's your email address? ")))

def validemail(s):
    if validators.email(s):
        return f"Valid"
    else:
        return f"Invalid"

if __name__ == "__main__":
    main()
