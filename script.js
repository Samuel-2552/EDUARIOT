const scene = new THREE.Scene();
const camera = new THREE.Camera();
scene.add(camera)
const renderer = new THREE.WebGLRenderer({
    antialias:true,
    alpha:true
});
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var ArToolkitSource = new THREEX.ArToolkitSource({
    sourceType: "webcam",

})
ArToolkitSource.init(function(){ 
    setTimeout(function(){
        ArToolkitSource.onResizeElement(); 
        ArToolkitSource.copyElementSizeTo(renderer.domElement);
    },2000)
})

var ArToolkitContext = new THREEX.ArToolkitContext({
    cameraParametersUrl: 'camera_para.dat',
    detectionMode: 'color_and_matrix'
});
ArToolkitContext.init(function(){ 
    camera.projectionMatrix.copy (ArToolkitContext.getProjectionMatrix());
});

var ArMarkerControls = new THREEX.ArMarkerControls(ArToolkitContext, camera,
{    
    type: 'pattern',
    patternUrl: 'pattern-hiro.patt',
    changeMatrixMode: 'cameraTransformMatrix'

});
scene.visible = false;

const geometry = new THREE.CubeGeometry(1,1,1);
const material = new THREE.MeshNormalMaterial( {
    transperent: true,
    opacity:0.5,
    side: THREE.Doubleside
  }  );    
const cube = new THREE.Mesh( geometry, material );
cube.position.y = geometry.parameters.height / 2;
scene.add( cube );

function animate() {
	requestAnimationFrame( animate );
    ArToolkitContext.update(ArToolkitSource.domElement);
    scene.visible = camera.visible;
    renderer.render( scene, camera );
};

animate();
