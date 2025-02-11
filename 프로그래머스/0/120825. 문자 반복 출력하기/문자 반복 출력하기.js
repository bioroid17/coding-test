function solution(my_string, n) {
    let result = "";
    for(s of my_string){
        result += s.repeat(n);
    }
    return result
}