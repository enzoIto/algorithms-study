fn main() {
    println!("Hello, world!");
}

fn largest_sum(nums: Vec<i32>) -> i32 {
    if nums.is_empty() {
        return 0
    }

    let mut second_last = 0;
    let mut last = 0;

    for num in nums {
        let new_last = std::cmp::max(last, second_last + num);
        second_last = last;
        last = new_last;
    }
    second_last
}
