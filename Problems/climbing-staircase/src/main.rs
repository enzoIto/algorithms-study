
fn main() {
    // should return 8
    climb_staircase(5);
}

fn climb_staircase(n: u32) -> u32 {
    let mut ways = vec![0; (n+1) as usize];
    ways[0] = 1;
    ways[1] = 1;
    for i in 2..(n+1) {
        ways[i as usize] = ways[(i-1) as usize] + ways[(i-2) as usize];
    }
    ways[n as usize]
}
