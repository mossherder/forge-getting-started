var dbId = 8293;
var frag_box = new THREE.Box3();
var node_box = new THREE.Box3();

var frag_ids = []
var instanceTree = viewer.model.getInstanceTree();
instanceTree.enumNodeFragments(dbId, function (fragId) {
    frag_ids.push(fragId);
});
var frag_list = viewer.model.getFragmentList();
frag_ids.forEach(function(fragId) {
	frag_list.getWorldBounds(fragId, frag_box);
	node_box.union(frag_box);
})
console.log(node_box)