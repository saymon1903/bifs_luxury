import { Canvas } from '@react-three/fiber';
import { Html, OrbitControls } from '@react-three/drei';

export default function HeroScene() {
  return (
    <Canvas className="h-screen">
      <ambientLight intensity={0.5} />
      <directionalLight position={[2, 2, 5]} />
      <mesh rotation={[0.4, 0.2, 0]}>
        <torusKnotGeometry args={[2.5, 0.8, 100, 20]} />
        <meshStandardMaterial color="#d4af37" wireframe />
      </mesh>
      <Html center>
        <h1 className="text-6xl font-serif text-gold">Kurbala</h1>
      </Html>
      <OrbitControls autoRotate enableZoom={false}/>
    </Canvas>
  );
}
