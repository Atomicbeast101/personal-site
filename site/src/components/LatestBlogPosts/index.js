import React from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import recentPosts from '@site/.docusaurus/docusaurus-plugin-content-blog/default/blog-post-list-prop-default.json';
import styles from './styles.module.css';

export default function LatestBlogPosts() {
  const latestPosts = recentPosts.items.slice(0, 6);

  return (
    <div className="container">
        <div className="row">
            {latestPosts.map((post, idx) => (
                <div key={idx} className="col col--4 margin-bottom--lg">
                    <div className="card padding--md" style={{ height: '100%' }}>
                        <div className="card__body">
                            <h3>{post.title}</h3>
                            <p>{post.description}</p>
                        </div>
                    </div>
                </div>
            ))}
        </div>
    </div>
  );
}