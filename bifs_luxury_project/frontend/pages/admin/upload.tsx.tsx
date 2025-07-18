import { useState } from 'react';

export default function Upload() {
  const [file, setFile] = useState<File|null>(null);
  const [msg, setMsg] = useState('');
  const submit = async () => {
    if (!file) return;
    const fd = new FormData();
    fd.append('file', file);
    fd.append('title', 'Test Product');
    fd.append('price', '9999');
    fd.append('description', 'Handwoven Rembo linen');
    fd.append('stock', '50');
    const res = await fetch('/api/admin/product', { method:'POST', body: fd,
      headers:{ Authorization:`Bearer ${localStorage.getItem('tok')}` }});
    setMsg(res.ok ? 'Uploaded' : 'Fail');
  };
  return (
    <div className="p-10">
      <input type="file" onChange={e=> setFile(e.target.files?.[0]||null)} />
      <button onClick={submit} className="ml-3 bg-gold text-royal px-4 py-1">Upload</button>
      <p>{msg}</p>
    </div>
  );
}
