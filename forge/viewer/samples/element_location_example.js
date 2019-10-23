var geometry = new THREE.SphereGeometry( 0.25, 32, 32 );
var material = new THREE.MeshBasicMaterial( {color: 0xffff00} );
geometry.applyMatrix( new THREE.Matrix4().makeTranslation(total_box.max.x, total_box.max.y, total_box.max.z) );
var sphere = new THREE.Mesh( geometry, material );
viewer.impl.scene.add(sphere)

//viewer.impl.scene.remove(sphere)
//viewer.impl.sceneUpdated(true)