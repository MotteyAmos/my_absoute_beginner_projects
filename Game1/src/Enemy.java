public class Enemy extends GameCharacter{
    private String type;

    public Enemy(String name, int hitPoints, int damagePoints, String type) {
        super(name, hitPoints, damagePoints);
        this.type = type;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public void takeDamage(int damage){
        this.setHitPoints(this.getHitPoints() - damage);
        System.out.println("you loose "+ damage + " points");
    }
}
