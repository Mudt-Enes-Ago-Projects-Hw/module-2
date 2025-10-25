import { useRouter } from 'next/router';

export default function Sidebar() {
  const router = useRouter();

  const menuItems = [
    {
      name: 'Home',
      path: '/',
    },
    {
      name: 'Search',
      path: '/search',
    },
    {
      name: 'Create',
      path: '/create',
    },
  ];

  return (
    <div className="w-64 min-h-screen bg-gradient-to-b from-gray-900 to-gray-800 text-white p-6 flex flex-col shadow-2xl sticky top-0">
      {/* Logo/Title */}
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-blue-600">
          Pharmacy
        </h1>
        <p className="text-gray-400 text-sm mt-1">Management System</p>
      </div>

      {/* Navigation Menu */}
      <nav className="flex flex-col gap-3 flex-1">
        {menuItems.map((item) => (
          <button
            key={item.path}
            onClick={() => router.push(item.path)}
            className={`
              group relative px-4 py-4 rounded-xl transition-all duration-300 text-left cursor-pointer
              ${router.pathname === item.path
                ? 'bg-gradient-to-r from-blue-600 to-blue-700 shadow-lg'
                : 'bg-gray-800 hover:bg-gray-700 hover:scale-105 hover:shadow-lg'
              }
            `}
          >
            <div className="flex items-center gap-3">
              <div className="font-semibold">{item.name}</div>
            </div>
            
            {/* Hover effect indicator */}
            <div className="absolute inset-0 rounded-xl border-2 border-transparent group-hover:border-blue-400 transition-colors pointer-events-none"></div>
          </button>
        ))}
      </nav>

      {/* Footer */}
      <div className="mt-auto pt-6 border-t border-gray-700">
        <p className="text-xs text-gray-400 text-center">
          Pharmacy Management v1.0
        </p>
      </div>
    </div>
  );
}
