import { useState, useEffect } from 'react';
import { useRouter } from 'next/router';
import { medicineApi } from '@/utils/api';

interface Medicine {
  id: string;
  name: string;
  description: string;
  price: number;
  stock: number;
  prescribed: boolean;
  company: string;
  created_at: string;
  updated_at: string;
}

export default function Home() {
  const router = useRouter();
  const [medicines, setMedicines] = useState<Medicine[]>([]);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchMedicines();
  }, []);

  const fetchMedicines = async () => {
    try {
      const response = await medicineApi.getAll();
      setMedicines(response.data);
    } catch (err) {
      setError('Failed to fetch medicines');
    }
  };


  if (error) {
    return (
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg">
        {error}
      </div>
    );
  }

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-800 mb-6">All Medicines</h1>
      
      {medicines.length === 0 ? (
        <div className="bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded-lg">
          No medicines found. Create one to get started!
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {medicines.map((medicine) => (
            <div
              key={medicine.id}
              onClick={() => router.push(`/search/${medicine.id}`)}
              className="bg-white rounded-lg shadow-lg p-6 cursor-pointer hover:shadow-xl transition-shadow"
            >
              <div className="flex justify-between items-start mb-3">
                <h2 className="text-xl font-bold text-gray-800">{medicine.name}</h2>
                {medicine.prescribed && (
                  <span className="px-2 py-1 bg-red-100 text-red-800 text-xs font-semibold rounded">
                    Rx
                  </span>
                )}
              </div>
              
              <p className="text-gray-600 text-sm mb-4 line-clamp-2">
                {medicine.description || 'No description'}
              </p>
              
              <div className="space-y-2 text-sm">
                <div className="flex justify-between">
                  <span className="text-gray-600">ID:</span>
                  <span className="font-mono text-gray-800">{medicine.id}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Price:</span>
                  <span className="font-semibold text-green-600">${medicine.price.toFixed(2)}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Stock:</span>
                  <span className={medicine.stock > 0 ? 'text-green-600' : 'text-red-600'}>
                    {medicine.stock} units
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-600">Company:</span>
                  <span className="text-gray-800 capitalize">{medicine.company}</span>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

