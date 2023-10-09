public class BankAccount extends AccountUser{
    private double balance = 0;
    private double interest;

    public void deposite(double amountOfDeposite){
        this.balance += amountOfDeposite;
    }

    public void withDraw(double amounntOfWithDraw){
        while (true){
            if ( amounntOfWithDraw > this.balance){
                this.balance -= amounntOfWithDraw;
                System.out.println("Your current balance is : " + this.balance);
                break;
            }
            else{
                System.out.println("Insufficient balance you have: "+ this.balance + " in your account");
                continue;
            }
        }
    }

    public void Calculateinterest(double interestRate){
        this.interest = interestRate * balance;
    }


}