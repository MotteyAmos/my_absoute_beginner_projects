public class GameCharacter{
    private String name;
    private int hitPoints;
    private int damagePoints;

    public GameCharacter(String name, int hitPoints, int damagePoints) {
        this.name = name;
        this.hitPoints = hitPoints;
        this.damagePoints = damagePoints;
    }
    public String getName(){
        return this.name;
    }
    public void setName(String name){
        this.name = name;
    }

    public int getHitPoints() {
        return hitPoints;
    }

    public void setHitPoints(int hitPoints) {
        this.hitPoints = hitPoints;
    }

    public int getDamagePoints() {
        return damagePoints;
    }

    public void setDamagePoints(int damagePoints) {
        this.damagePoints = damagePoints;
    }

    public void attack(GameCharacter character){
        character.hitPoints -= this.damagePoints;
    }
}
