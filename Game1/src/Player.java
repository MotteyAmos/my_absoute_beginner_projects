public class Player extends GameCharacter{
    private int level;
    private int experiencePoints;

    public Player(String name, int hitPoints, int damagePoints, int level, int experiencePoints) {
        super(name, hitPoints, damagePoints);
        this.level = level;
        this.experiencePoints = experiencePoints;
    }

    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }

    public int getExperiencePoints() {
        return experiencePoints;
    }

    public void setExperiencePoints(int experiencePoints) {
        this.experiencePoints = experiencePoints;
    }

    public void gainExperience(int experience) {
        this.experiencePoints += experience;
        int experienceToNextLevel = this.level * 10;
        if (this.experiencePoints >= experienceToNextLevel) {
            this.level++;
            this.setHitPoints(this.getHitPoints() + 10);
            this.setDamagePoints(this.getDamagePoints() + 5);
            System.out.println(this.getName() + " has reached level " + this.level + " and gained 10 hit points and 5 damage points!");
        }
    }
}

