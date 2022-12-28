use std::collections::BTreeSet;
fn main() {
    fun(vec![10,15,3,7],17);
}


fn fun(arr: Vec<i32>, k: i32) -> bool {
    let mut seen = BTreeSet::new();
    for index in 0..arr.len() {
        if seen.contains(&(k - arr[index])) {
            return true;
        }
        seen.insert(arr[index]);
    }
    return false;
}
