import { useRouter } from 'next/router';

interface NotFoundProps {
  message?: string;
  messageTwo?: string;
}

export default function NotFound({ message = 'Medicine Not Found', messageTwo = 'The page you are looking for does not exist.' }: NotFoundProps) {
  const router = useRouter();

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full text-center">
        <div className="bg-white rounded-2xl shadow-xl p-12">
          <div className="text-9xl font-bold text-gray-300 mb-4">404</div>
          <h1 className="text-3xl font-bold text-gray-800 mb-4">{message}</h1>
          <p className="text-gray-600 mb-8">{messageTwo}</p>
          <div className="space-y-3">
            <button
              onClick={() => router.push('/search')}
              className="w-full px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-semibold cursor-pointer"
            >
              Go to Search
            </button>
            <button
              onClick={() => router.push('/')}
              className="w-full px-6 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors font-semibold cursor-pointer"
            >
              Go to Home
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
