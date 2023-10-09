public class Main {
    public static void main(String[] args){
        Player playerOb1 = new Player("Batman", 90,15,1,15);
        Enemy enemy1 = new Enemy("Jokeman", 70,19,"enemy");

        while (true){
            playerOb1.attack(enemy1);
            enemy1.attack(playerOb1);

            if (playerOb1.getHitPoints() <= 0 || enemy1.getHitPoints() <= 0){
                if (playerOb1.getHitPoints() > enemy1.getHitPoints()){
                    System.out.println("playerOb1 has won");
                }
                else{
                    System.out.println("enemy1 has won");
                }
                break;
            }
            else{
                continue;
            }
        }
    }
}
