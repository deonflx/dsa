class romantoint {
    public int romanToInt(String s) {
        int result=0;
        int []arr;
        arr=new int[s.length()];
        for(int i=0;i<s.length();i++)
        {char c=s.charAt(i);
        switch(c)
        {case'M':
        arr[i]=1000;
        break;
        case'D':
        arr[i]=500;
        break;
        case'C':
        arr[i]=100;
        break;
        case'L':
        arr[i]=50;
        break;
        case'X':
        arr[i]=10;
        break;
        case'V':
        arr[i]=5;
        break;
        case'I':
        arr[i]=1;
        break;
        default:
        System.out.println("wrong choice");
        break;}      }
        for(int i=0;i<arr.length;i++)
        {if(i!=arr.length-1)
         {   if(arr[i]<arr[i+1])
            {result=result+arr[i+1]-arr[i];
            i++;}
            else if(arr[i]==arr[i+1]){
                arr[i+1]=arr[i]+arr[i+1];
            }
            else{
                result+=arr[i];
            }}
        else{
             result+=arr[i];
        }    
        }  return result;}}