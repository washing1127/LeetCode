/**
 * @Author: washing
 * @DateTime: 2021/3/19 10:29
 * @File: 1603.java
 * @Desc: 
 **/
class ParkingSystem {

    int[] space = new int[4];
    public ParkingSystem(int big, int medium, int small) {
        space[0] = 0;
        space[1] = big;
        space[2] = medium;
        space[3] = small;
    }
    
    public boolean addCar(int carType) {
        return --space[carType] >= 0;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */