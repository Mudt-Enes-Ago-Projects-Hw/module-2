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
    company_id: number;
  }) => api.post('/medicines', data),

  // Update medicine
  update: (id: string, data: Partial<{
    name: string;
    description: string;
    price: number;
    stock: number;
    prescribed: boolean;
    company_id: number;
  }>) => api.put(`/medicines/${id}`, data),

  // Delete medicine
  delete: (id: string) => api.delete(`/medicines/${id}`),

  // Search medicines
  search: (query: string) => api.get(`/medicines/search?q=${query}`),
};

// Company API calls
export const companyApi = {
  // Get all companies
  getAll: () => api.get('/companies'),

  // Get company by ID
  getById: (id: number) => api.get(`/companies/${id}`),

  // Create new company
  create: (data: {
    name: string;
    code: string;
    description: string;
  }) => api.post('/companies', data),

  // Update company
  update: (id: number, data: Partial<{
    name: string;
    code: string;
    description: string;
  }>) => api.put(`/companies/${id}`, data),

  // Delete company
  delete: (id: number) => api.delete(`/companies/${id}`),
};

export default api;
