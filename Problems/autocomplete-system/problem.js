// simpler solution, O(n) time complexity
function autocomplete(s, array) {
  let matches = array.filter(x => x.startsWith(s));
  return matches;
}

let array = ['dog', 'deer', 'deal'];
let s = 'de';
console.log(autocomplete(s, array));  // ['deer', 'deal']


// optimal solution

class Trie {
  constructor() {
    this.root = new TrieNode();
  }

  insert(word) {
    let node = this.root;
    for (let i = 0; i < word.length; i++) {
      let c = word.charAt(i);
      if (!node.children[c]) {
        node.children[c] = new TrieNode();
      }
      node = node.children[c];
    }
    node.isWord = true;
  }

  search(s) {
    let node = this.root;
    for (let i = 0; i < s.length; i++) {
      let c = s.charAt(i);
      if (!node.children[c]) {
        return [];
      }
      node = node.children[c];
    }

    let results = [];
    this._dfs(node, s, results);
    return results;
  }

  _dfs(node, s, results) {
    if (node.isWord) {
      results.push(s);
    }
    for (let c in node.children) {
      this._dfs(node.children[c], s + c, results);
    }
  }
}

class TrieNode {
  constructor() {
    this.children = {};
    this.isWord = false;
  }
}

let trie = new Trie();
trie.insert('dog');
trie.insert('deer');
trie.insert('deal');
console.log(trie.search('de'));  // ['deer', 'deal']
