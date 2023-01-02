
use std::collections::HashMap;

fn main() {
    println!("Hello, world!");
}


struct Node {
    data: i32,
    both: usize,
}

struct XorLinkedList {
    nodes: HashMap<usize, Node>,
}

impl XorLinkedList {
    fn new() -> Self {
        Self { nodes: HashMap::new() }
    }

    fn add(&mut self, element: i32) {
        let new_node = Node {
            data: element,
            both: 0,
        };

        let new_node_ptr = get_pointer(&new_node);
        let new_node_address = dereference_pointer(new_node_ptr);

        if let Some(last_node) = self.nodes.values().last() {
            let last_node_ptr = get_pointer(last_node);
            let last_node_address = dereference_pointer(last_node_ptr);

            last_node.both = last_node.both ^ new_node_address;
            new_node.both = last_node_address;

            self.nodes.insert(new_node_address, new_node);
        } else {
            self.nodes.insert(new_node_address, new_node);
        }
    }

    fn get(&self, index: usize) -> Option<&Node> {
        let mut prev_address = 0;
        let mut current_address = self.nodes.keys().nth(index)?;

        for (i, (address, node)) in self.nodes.iter().enumerate() {
            if i == index {
                return Some(node);
            }

            let next_address = prev_address ^ node.both;
            prev_address = *address;
            current_address = next_address;
        }

        None
    }
}
