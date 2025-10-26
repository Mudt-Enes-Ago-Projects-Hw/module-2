import { useRouter } from 'next/router';
import { useState, useEffect } from 'react';
import { medicineApi, companyApi } from '@/utils/api';
import { toast } from 'react-toastify';
import NotFound from '@/components/NotFound';

interface Medicine {
  id: string;
  name: string;
  description: string;
  price: number;
  stock: number;
  prescribed: boolean;
  company_id: number;
  company: {
    id: number;
    name: string;
    code: string;
    description: string;
  };
  created_at: string;
  updated_at: string;
}

interface Company {
  id: number;
  name: string;
  code: string;
  description: string;
}

export default function SearchMedicine() {
  const router = useRouter();
  const { id } = router.query;
  
  const [medicine, setMedicine] = useState<Medicine | null>(null);
  const [companies, setCompanies] = useState<Company[]>([]);
  const [error, setError] = useState('');
  const [isEditing, setIsEditing] = useState(false);
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    price: 0,
    stock: 0,
    prescribed: false,
    company_id: 0,
  });

  useEffect(() => {
    if (id) {
      fetchMedicine();
      fetchCompanies();
    }
  }, [id]);

  const fetchCompanies = async () => {
    try {
      const response = await companyApi.getAll();
      setCompanies(response.data);
    } catch (err) {
      console.error('Failed to fetch companies', err);
    }
  };

  const fetchMedicine = async () => {
    try {
      setError('');

      const response = await medicineApi.getById(id as string);

      setMedicine(response.data);

      setFormData({
        name: response.data.name,
        description: response.data.description,
        price: response.data.price,
        stock: response.data.stock,
        prescribed: response.data.prescribed,
        company_id: response.data.company_id,
      });
    } catch (err: any) {
      const errorMessage = err.response?.data?.error || 'Medicine not found';
      setError(errorMessage);
    }
  };

  const handleUpdate = async () => {
    try {
      setError('');

      await medicineApi.update(id as string, formData);
      
      toast.success('Medicine updated successfully!');

      setIsEditing(false);
      fetchMedicine();

    } catch (err: any) {

      const errorMessage = err.response?.data?.error || 'Failed to update medicine';
      toast.error(errorMessage);
      setError(errorMessage);
    
    }
  };  
  
  const handleDelete = async () => {
    if (confirm('Are you sure you want to delete this medicine?')) {

      try {
        await medicineApi.delete(id as string);
        toast.success('Medicine deleted successfully!');
        router.push('/');

      } catch (err: any) {

        const errorMessage = err.response?.data?.error || 'Failed to delete medicine';
        toast.error(errorMessage);
        setError(errorMessage);

      }
    }
  };

  if (error && !medicine) {
    return <NotFound message={error} />;
  }

  return (
    <div className="max-w-4xl mx-auto">
      <div className="bg-white rounded-lg shadow-lg p-8">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-3xl font-bold text-gray-800">
            {isEditing ? 'Edit Medicine' : 'Medicine Details'}
          </h1>
          <div className="flex gap-2">
            {!isEditing ? (
              <>
                <button
                  onClick={() => setIsEditing(true)}
                  className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors cursor-pointer"
                >
                  Edit
                </button>
                <button
                  onClick={handleDelete}
                  className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors cursor-pointer"
                >
                  Delete
                </button>
              </>
            ) : (
              <>
                <button
                  onClick={handleUpdate}
                  className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors cursor-pointer"
                >
                  Save
                </button>
                <button
                  onClick={() => {
                    setIsEditing(false);
                    setFormData({
                      name: medicine!.name,
                      description: medicine!.description,
                      price: medicine!.price,
                      stock: medicine!.stock,
                      prescribed: medicine!.prescribed,
                      company_id: medicine!.company_id,
                    });
                  }}
                  className="px-4 py-2 bg-gray-600 text-white rounded-lg hover:bg-gray-700 transition-colors cursor-pointer"
                >
                  Cancel
                </button>
              </>
            )}
          </div>
        </div>

        {error && (
          <div className="mb-4 bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg">
            {error}
          </div>
        )}

        <div className="space-y-4">
          {/* ID (Read-only) */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Medicine ID
            </label>
            <input
              type="text"
              value={medicine?.id || ''}
              disabled
              className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100 text-gray-600"
            />
          </div>

          {/* Name */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Name
            </label>
            <input
              type="text"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              disabled={!isEditing}
              className={`w-full px-3 py-2 border border-gray-300 rounded-lg ${
                isEditing ? 'bg-white' : 'bg-gray-100 text-gray-600'
              }`}
            />
          </div>

          {/* Description */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Description
            </label>
            <textarea
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              disabled={!isEditing}
              rows={3}
              className={`w-full px-3 py-2 border border-gray-300 rounded-lg ${
                isEditing ? 'bg-white' : 'bg-gray-100 text-gray-600'
              }`}
            />
          </div>

          {/* Price */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Price ($)
            </label>
            <input
              type="number"
              step="0.01"
              value={formData.price}
              onChange={(e) => setFormData({ ...formData, price: parseFloat(e.target.value) })}
              disabled={!isEditing}
              className={`w-full px-3 py-2 border border-gray-300 rounded-lg ${
                isEditing ? 'bg-white' : 'bg-gray-100 text-gray-600'
              }`}
            />
          </div>

          {/* Stock */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Stock
            </label>
            <input
              type="number"
              value={formData.stock}
              onChange={(e) => setFormData({ ...formData, stock: parseInt(e.target.value) })}
              disabled={!isEditing}
              className={`w-full px-3 py-2 border border-gray-300 rounded-lg ${
                isEditing ? 'bg-white' : 'bg-gray-100 text-gray-600'
              }`}
            />
          </div>

          {/* Prescribed */}
          <div>
            <label className="flex items-center space-x-2">
              <input
                type="checkbox"
                checked={formData.prescribed}
                onChange={(e) => setFormData({ ...formData, prescribed: e.target.checked })}
                disabled
                className="w-4 h-4"
              />
              <span className="text-sm font-medium text-gray-700">
                Requires Prescription
              </span>
            </label>
          </div>

          {/* Company */}
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-1">
              Company
            </label>
            <input
              type="text"
              value={medicine?.company.name || ''}
              disabled
              className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100 text-gray-600"
            />
            <p className="mt-1 text-sm text-gray-500">
              Company Code: {medicine?.company.code}
            </p>
          </div>

          {/* Timestamps */}
          <div className="grid grid-cols-2 gap-4 pt-4 border-t">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Created At
              </label>
              <input
                type="text"
                value={medicine?.created_at ? new Date(medicine.created_at).toLocaleString() : ''}
                disabled
                className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100 text-gray-600 text-sm"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                Updated At
              </label>
              <input
                type="text"
                value={medicine?.updated_at ? new Date(medicine.updated_at).toLocaleString() : ''}
                disabled
                className="w-full px-3 py-2 border border-gray-300 rounded-lg bg-gray-100 text-gray-600 text-sm"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
