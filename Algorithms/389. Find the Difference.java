class Solution {
    public char findTheDifference(String s, String t) {
        int[] a=new int[26];
        for(int i=0;i<t.length();i++){
            int index=t.charAt(i)-'a';
            a[index]+=1;
        }
        for(int i=0;i<s.length();i++){
            int index=s.charAt(i)-'a';
            a[index]-=1;
        }
        for(int i=0;i<26;i++){
            if(a[i]>0){
                return (char)('a'+i);
            }
        }
        return 'a';
    }
}