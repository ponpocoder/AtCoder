use proconio::input;
fn main() {
    input! {
        n: usize,
        mut s: [String; n],
    }

    s.reverse();
    for s in s {
        println!("{}", s);
    }
}
