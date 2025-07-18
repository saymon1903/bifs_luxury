import { motion } from 'framer-motion';
import Head from 'next/head';
import useSWR from 'swr';
import Link from 'next/link';
import dynamic from 'next/dynamic';

const fetcher = (url: string) => fetch(url).then(r => r.json());
const Scene = dynamic(() => import('../components/HeroScene'), { ssr: false });

export default function Home() {
  const { data } = useSWR('/api/catalog', fetcher);
  return (
    <>
      <Head><title>BIFS Luxury</title></Head>
      <Scene />
      <section className="mx-auto max-w-7xl p-6 grid md:grid-cols-3 gap-6">
        {data?.map((p:any) => (
          <motion.div key={p.id}
            whileHover={{ scale: 1.05 }} className="bg-royal text-white p-4 rounded">
            <img src={p.thumbnail} className="w-full h-64 object-cover" />
            <h3 className="font-serif text-xl mt-2">{p.title}</h3>
            <p className="text-gold font-semibold">৳ {p.price}</p>
            <Link href={`/product/${p.slug}`}>
              <button className="mt-2 px-4 py-1 bg-gold text-royal rounded">View</button>
            </Link>
          </motion.div>
        ))}
      </section>
    </>
  );
}
