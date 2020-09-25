class Solution {
    public String multiply(String num1, String num2) {
        if(num1.length()==0 || num2.length()==0) return "0";
        if(num1.length()<num2.length()){
            String temp=num1;
            num1=num2;
            num2=temp;
        }
        int[] ans=new int[1000];
        for(int i=num2.length()-1;i>=0;i--){
            int x=num2.charAt(i)-'0',carry=0;
            for(int j=num1.length()-1;j>=0;j--){
                int y=num1.charAt(j)-'0';
                int z=x*y+carry;
                carry = z/10;
                z=z%10;
                int index=num2.length()-1-i+num1.length()-1-j;
                ans[index]+=z;
                carry+=ans[index]/10;
                ans[index]=ans[index]%10;
            }
            if(carry>0){
                int index = num2.length()-1-i+num1.length();
                ans[index]+=carry;
                ans[index+1]+=ans[index]/10;
                ans[index]%=10;
            }
        }
        int index = num2.length()+num1.length();
        if(ans[index]>=10){
            ans[index+1]+=ans[index]/10;
            ans[index]%=10;
        }
        boolean start=false;
        String res="";
        for(int i=index+1;i>=0;i--){
            if(start || (ans[i]>0)){
                res=res+(char)(ans[i]+'0');
                start=true;
            }
        }
        if(res.equals("")) return "0";
        return res;
    }
}