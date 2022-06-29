class Solution {
    public int getSum(int a, int b) {
        while(b != 0){
            int carrymask = (a&b)<<1;
            a = a ^ b;
            b = carrymask;
        }
        return a;
    }
}