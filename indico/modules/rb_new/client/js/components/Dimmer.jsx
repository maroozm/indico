/* This file is part of Indico.
 * Copyright (C) 2002 - 2018 European Organization for Nuclear Research (CERN).
 *
 * Indico is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License as
 * published by the Free Software Foundation; either version 3 of the
 * License, or (at your option) any later version.
 *
 * Indico is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Indico; if not, see <http://www.gnu.org/licenses/>.
 */

import React from 'react';
import PropTypes from 'prop-types';
import {Image} from 'semantic-ui-react';

import './Dimmer.module.scss';
import SpriteImage from './SpriteImage';


export default class DimmableImage extends React.Component {
    static propTypes = {
        src: PropTypes.oneOfType([
            PropTypes.string,
            PropTypes.func
        ]).isRequired,
        content: PropTypes.node,
        hoverContent: PropTypes.node,
        spritePos: PropTypes.number
    };

    static defaultProps = {
        content: null,
        hoverContent: null,
        spritePos: null
    };

    render() {
        const {src, content, hoverContent, spritePos} = this.props;

        return (
            <div styleName="dimmable-image">
                {spritePos === null
                    ? <Image src={src} className="img" />
                    : <SpriteImage src={src} pos={spritePos} />
                }
                <div styleName="content">
                    {content}
                </div>
                <div styleName="hover-content">
                    {hoverContent}
                </div>
            </div>
        );
    }
}
