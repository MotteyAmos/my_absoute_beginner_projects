public class Main extends Admistrator {

    public static void main(String[] args) {
        Admistrator admistrator1 = new Admistrator();

        admistrator1.createUsers();
        for (int i=0; i< bankAccountUsers.length; i++){
            System.out.println(bankAccountUsers[i]);
        }
    }
}