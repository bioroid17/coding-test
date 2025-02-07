function solution(array) {
    if(array.length === 1){
        return array[0];
    }
    let countArr = Array.from({length:Math.max(...array)+1}, (v,i) => 0);
    for(num of array){
        countArr[num]++;
    }
    let maxCount = 0;
    let mode = 0;
    let check = false;
    countArr.forEach((count, index) => {
        if(count > maxCount){
            maxCount = count;
            mode = index;
            check = false;
        } else if(count === maxCount) {
            check = true;
        }
    })
    return check ? -1 : mode;
}