class Log {
  constructor(size) {
    this.size = size
    this.buffer = new Array(size)
    this.head = -1
  }

  record(order_id) {
    this.head = (this.head + 1) % this.size
    this.buffer[this.head] = order_id
  }

  get_last(i) {
    if (this.head === -1) {
      return -1
    }

    let index = (this.head -i + this.size) % this.size
    return this.buffer[index];
  }  
}