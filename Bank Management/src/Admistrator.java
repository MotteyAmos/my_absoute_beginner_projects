class BankAccountUsers{

}
public class Admistrator extends BankAccount{
    public static  BankAccount bankAccountUsers[] = new BankAccount[9];
    public  void createUsers(){
        for (int i=0 ; i< 5; i++){
            BankAccount user = new BankAccount();
            user.CreateUser();
            bankAccountUsers[ i] =  user;

        }
    }
}
