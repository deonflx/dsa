class Solution {
    public int[] twoSum(int[] nums, int target) {
        int []arr;
        arr=new int[2];
        for(int i=0;i<(nums.length);i++)
        {for (int j=1;j<(nums.length);j++)
        {if(nums[i]+nums[j]==target && i!=j)
        {arr[0]=i;
        arr[1]=j;
            return arr ;}}}return arr;}
            }

        
    

        