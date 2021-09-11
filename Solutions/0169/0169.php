<!-- Author: washing
DateTime: 2021/1/26 18:44
File: 0169.php
Desc:  -->

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function majorityElement($nums) {
        $a=0;
        $c=0;
        for ($i=0; $i<count($nums); $i++) {
            $n=$nums[$i];
            if ($c==0){
                $a=$n;
                $c++;
            }else if ($a==$n){
                $c++;
            }else{
                $c--;
            }
        }
        return $a;
    }
}