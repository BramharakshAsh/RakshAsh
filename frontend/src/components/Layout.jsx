import React from 'react';
import Chat from './Chat';

export default function Layout() {
  return (
    <div className="h-screen flex">
      <div className="w-1/3 border-r"><Chat /></div>
      <div className="w-2/3 p-4">Code editor and console here</div>
    </div>
  );
}
