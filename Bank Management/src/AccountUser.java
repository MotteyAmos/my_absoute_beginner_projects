import java.util.Scanner;

public class AccountUser{
    private String fullName, address, email, contact, dateOfBirth;
    private int  accountNumber;

    public void setFullName(String fullName){
        this.fullName =  fullName;
    }

    public String getFullName(){
        return this.fullName;
    }
    public void setAddress(String address){
        this.address = address;
    }
    public String getAddress(){
        return this.address;
    }
    public void setEmail(String email){
        this.email = email;
    }
    public String getEmail(String email){
        return this.email;
    }
    public void setAccounNumber(int accountNumber){
        this.accountNumber = accountNumber;
    }
    public int getAccountNumber(){
        return this.accountNumber;
    }
    public void setContact(String contact){
        this.contact = contact;
    }
    public String getContact(){
        return this.contact;
    }
    public void setDateOfBirth(String dateOfBirth){
        this.dateOfBirth = dateOfBirth;
    }
    public String getDateOfBirth(){
        return this.dateOfBirth;
    }

    public  void CreateUser(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your full name: ");
        this.setFullName(scanner.nextLine());
        System.out.println("Enter your address: ");
        this.setAddress(scanner.nextLine());
        System.out.println("Enter your address");
        this.setEmail(scanner.nextLine());
        System.out.println("Enter your contact: ");
        this.setContact(scanner.nextLine());
        System.out.println("Enter your data of birth");
        this.setDateOfBirth(scanner.nextLine());
    }
}


