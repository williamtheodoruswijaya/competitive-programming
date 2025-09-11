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
                if (this.big < 0) {
                    return false;
                } else {
                    return true;
                }
            case 2:
                if (this.medium < 0) {
                    return false;
                } else {
                    return true;
                }
            case 3:
                if (this.small < 0) {
                    return false;
                } else {
                    return true;
                }
        }
        return true;
    }
    
    public boolean addCar(int carType) {
        boolean canPark = true;
        switch(carType) {
            case 1:
                this.big--;
                return checkPark(carType);
            case 2:
                this.medium--;
                return checkPark(carType);
            case 3:
                this.small--;
                return checkPark(carType);
        }

        return canPark;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */