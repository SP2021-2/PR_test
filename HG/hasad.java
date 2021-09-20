class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int tmp = x;
        int num = 0;
        while(tmp > 0){
            num += tmp % 10;
            tmp = tmp / 10;
        }
        
        // System.out.println(x+","+num);
        
        answer = x%num==0?true:false;
        
        return answer;
    }
}