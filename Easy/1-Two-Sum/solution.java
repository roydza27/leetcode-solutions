class Solution {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        int[] newArray = new int[n];

        for(int i=0;i<n;i++){
            newArray[i] = nums[i];
        }

        for(int i = 0;i<n;i++){
            for(int j = 0; j <i;j++){
                if(newArray[i]+newArray[j] == target){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }
}