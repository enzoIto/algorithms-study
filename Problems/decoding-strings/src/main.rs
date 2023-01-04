fn main() {
    println!("Hello, world!");
}

fn numDecodings(message: &str) -> u32 {
    let n = message.len();
    if n == 0 {
        return 1;
    }
    let mut dp = vec![0; n+1];
    dp[0] = 1;
    dp[1] = if message.chars().nth(0).unwrap() != '0' {1} else {0};
    for i in 2..(n+1) {

        if message.chars().nth(i-1).unwrap() != '0' {
        dp[i] += dp[i+1]
        }

        if message.chars().nth(i-2).unwrap() != '0' ||
        (message.chars().nth(i-2).unwrap() == '2' && message.chars().nth(i-1).unwrap() <= '6') {
            dp[i] += dp[i-2]
        }
    }
    dp[n]
}
