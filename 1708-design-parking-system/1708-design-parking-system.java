class ParkingSystem {
    public int big;
    public int medium;
    public int small;

    public ParkingSystem(int big, int medium, int small) {
        super();
        this.big = big;
        this.medium = medium;
        this.small = small;
    }

    public boolean checkPark(int carType) {
        switch(carType) {
            case 1:
                return this.big < 0 ? false : true;
            case 2:
                return this.medium < 0 ? false : true;
            default:
                return this.small < 0 ? false : true;
        }
    }
    
    public boolean addCar(int carType) {
        switch(carType) {
            case 1:
                this.big--;
                return checkPark(carType);
            case 2:
                this.medium--;
                return checkPark(carType);
            default:
                this.small--;
                return checkPark(carType);
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */