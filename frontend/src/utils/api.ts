import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3001';

const api = axios.create({
  baseURL: `${API_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Medicine API calls
export const medicineApi = {
  // Get all medicines
  getAll: () => api.get('/medicines'),

  // Get medicine by ID
  getById: (id: string) => api.get(`/medicines/${id}`),

  // Create new medicine
  create: (data: {
    name: string;
    description: string;
    price: number;
    stock: number;
    prescribed: boolean;
    company: string;
  }) => api.post('/medicines', data),

  // Update medicine
  update: (id: string, data: Partial<{
    name: string;
    description: string;
    price: number;
    stock: number;
    prescribed: boolean;
    company: string;
  }>) => api.put(`/medicines/${id}`, data),

  // Delete medicine
  delete: (id: string) => api.delete(`/medicines/${id}`),

  // Search medicines
  search: (query: string) => api.get(`/medicines/search?q=${query}`),
};

export default api;
